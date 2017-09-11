import boto3
import StringIO
import zipfile
import mimetypes

def lambda_handler(event, context):
    s3 = boto3.resource('s3')
    sns = boto3.resource('sns', region_name='eu-west-2')
    topic = sns.Topic('arn:aws:sns:eu-west-2:766192781453:deployServerlessPortfolioTopic')

    try:
        portfolio_bucket = s3.Bucket('serverless.rootofpi.co.uk')
        build_bucket = s3.Bucket('serverless-portfolio')

        portfolio_zip = StringIO.StringIO()

        build_bucket.download_fileobj('serverlessbuild.zip',portfolio_zip)

        with zipfile.ZipFile(portfolio_zip) as myzip:
            for nm in myzip.namelist():
                obj = myzip.open(nm)
                portfolio_bucket.upload_fileobj(obj, nm,
                # Remember mimetypes guesses using file extension so make sure exists!
                ExtraArgs={'ContentType': mimetypes.guess_type(nm)[0]})
                portfolio_bucket.Object(nm).Acl().put(ACL='public-read')

        topic.publish(Subject="Serverless Portfolio", Message="Serverless Portfolio Deployed Successfully")
        print "Job Complete."

    except:
        topic.publish(Subject="Serverless Portfolio Deployment Failed", Message="Serverless Portfolio Not Deployed Successfully")
        print "Job not successful."
