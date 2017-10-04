import React from 'react';
import ReactDOM from 'react-dom';
// import new custom react component
import ExampleWork from './example-work';

const myWork = [
  {
    'title': "All You Need",
    'image': {
      'desc': "example image of a cat.",
      'source': "images/example3.png",
      'comment': `“Bengal cat” by roberto shabs is licensed under CC BY 2.0
           https://www.flickr.com/photos/37287295@N00/2540855181`
    }
  },
  {
    'title': "AWS Lambda Snapshot Backup & Prune",
    'image': {
      'desc': "example screenshot of a project involving code",
      'source': "images/example1.png",
      'comment': "probably doesn't even compile"
    }
  },
  {
    'title': "Salesforce Administration Areas",
    'image': {
      'desc': "chemistry shots",
      'source': "images/example2.png",
      // use backticks to use javascript template string, on multi line
      'comment': `“Chemistry” by Surian Soosay is licensed under CC BY 2.0
          https://www.flickr.com/photos/ssoosay/4097410999 `
    }
  }
]
ReactDOM.render(<ExampleWork work={myWork}/>, document.getElementById('example-work'));
