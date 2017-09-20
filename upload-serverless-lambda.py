import boto3
import StringIO
import zipfile
import mimetypes

def lambda_handler(event, context):
    sns = boto3.resource('sns', region_name='eu-west-2')
    topic = sns.Topic('arn:aws:sns:eu-west-2:766192781453:deployServerlessPortfolioTopic')

    location = {
        "bucketName":'serverless-portfolio',
        "objectKey": 'serverlessbuild.zip'
    }

    # check to see if the job was triggered by codepipeline
    try:
        job = event.get("CodePipeline.job")
        if job:
            print "Lambda triggered from codepipeline event"
            for artifact in job["data"]["inputArtifacts"]:
                if artifact["name"] == "MyAppBuild":
                    location = artifact["location"]["s3Location"]
        print "Building portfolio from " + str(location)

        s3 = boto3.resource('s3')

        portfolio_bucket = s3.Bucket('serverless.rootofpi.co.uk')
        build_bucket = s3.Bucket(location["bucketName"])

        portfolio_zip = StringIO.StringIO()

        build_bucket.download_fileobj(location["objectKey"],portfolio_zip)

        with zipfile.ZipFile(portfolio_zip) as myzip:
            for nm in myzip.namelist():
                obj = myzip.open(nm)
                portfolio_bucket.upload_fileobj(obj, nm,
                # Remember mimetypes guesses using file extension so make sure exists!
                ExtraArgs={'contentType': mimetypes.guess_type(nm)[0]})
                portfolio_bucket.Object(nm).Acl().put(ACL='public-read')

        if job:
            codepipeline = boto3.client('codepipeline')
            codepipeline.put_job_success_result(jobId=job["id"])
        topic.publish(Subject="Serverless Portfolio", Message="Serverless Portfolio Deployed Successfully")
        print "Job Complete."

    except:
        #if job:c
        #    codepipeline = boto3.client('codepipeline')
        #    codepipeline.put_job_failure_result(jobId=job["id"], failureDetails=message["JobFailed"])
        topic.publish(Subject="Serverless Portfolio Deployment Failed", Message="Serverless Portfolio Not Deployed Successfully")

        raise
        print "Job not successful."
