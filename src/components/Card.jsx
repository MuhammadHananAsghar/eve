import React from "react";
import '../styles/Main.css';

const Card = (props) => {

  const play = (videoTitle, videoID) => {
    window.location.href = `/player/${videoTitle}/${videoID}`;
  }


    return (
        <div className="cardd" onClick={() => {play(props.mtitle, props.id)}}>
          <div className="image">
            <img
              alt={props.owner}
              src={props.thumb}
            />
          </div>
          <div className="details">
            <img
              alt={'al'}
              src={props.cimage}
            />
            <div className="meta">
              <h5>{props.title}</h5>
              <span>{props.owner}</span>
              <div className="time">
            <span>{props.views}&nbsp;&nbsp;<span id="dot">.</span>&nbsp;&nbsp;{props.date}</span>
          </div>
            </div>
          </div>
        </div>
    );
}

export default Card;