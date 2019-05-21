import React, { Component } from 'react';


class Likert extends Component{
    constructor(props){
        super(props)
        this.state = {
          number:1

        }
    }
    answerNum = () => {
      let { number } = this.state
      let number = number + 1
      this.setState({number:number})
    }

    render() {
      let { number } = this.state
        return(
          <div>
            <div id="likert">
                <label id= "QNum"{number} name="AnsNum">{number}: </label>

                <label>A:</label>
                <input type="radio" name= {number} value="A">

                <label>B:</label>
                <input type="radio" name= {number} value="B">

                <label>C:</label>
                <input type="radio" name={number} value="C">

                <label>D:</label>
                <input type="radio" name={number} value="D">

                <label>E:</label>
                <input type="radio" name={number} value="E">
            </div>
            <button onClick= {this.answerNum}>Add A question to Test</button>
          </div>


        )
    }
}

export default Likert
