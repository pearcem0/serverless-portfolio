import React from 'react';

class ExampleWork extends React.Component {
  render() {
    return (
      <section className="section section--alignCentered section--description">
      {/* every array in javascript comes with a map
       map is a function that takes another function as an argument
       call x times for x number of items in the array */}
      { this.props.work.map( (example, idx) => {
        return (
          <ExampleWorkBubbles example={example} key={idx}/>
        )
        }
        )
      }
      </section>
    )
  }
}
class ExampleWorkBubbles extends React.Component {
  render() {
    let example = this.props.example;
    return (
      // remember class is a reserved word in javascript, so we can't use in jsx
        <div className="section__exampleWrapper">
          <div className="section__example">
            <img alt={ example.image.desc }
                 className="section__exampleImage"
                 src={ example.image.source }/>
            <dl className="color--cloud">
              <dt className="section__exampleTitle section__text--centered">
                { example.title }
              </dt>
              <dd></dd>
            </dl>
          </div>
        </div>
    )
  }

}
// in order to import in main.js we first need to export
// each file can have ONE default export
export default ExampleWork;
