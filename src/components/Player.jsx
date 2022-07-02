import React from "react";
import ReactPlayer from "react-player/lazy";
import "../styles/Player.css";
import { IoArrowBackSharp } from "react-icons/io5";
import { useParams, useNavigate } from "react-router-dom";

export const Player = () => {
  const { title, id } = useParams();
  const navigate = useNavigate();
  const url = `https://www.youtube.com/watch?v=${id}`;
  return (
    <div className="player">
      {id ? (
        <div className="pl">
          <h2 className="title">{title}</h2>
          <ReactPlayer
            url={url}
            width={"100%"}
            height={"100%"}
            controls={true}
          />
          <div className="button" onClick={() => navigate("/")}>
            <IoArrowBackSharp />
            &nbsp;Back
          </div>
        </div>
      ) : (
        <div style={{color: "white"}}>Error Here</div>
      )}
    </div>
  );
};
