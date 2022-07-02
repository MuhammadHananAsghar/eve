import React, { useRef } from "react";
import "../styles/Navbar.css";
import { BiSearchAlt } from "react-icons/bi";
import { MdOutlineKeyboardVoice } from "react-icons/md";
import { useNavigate } from "react-router-dom";
import avatar from "../images/avatar.jpg";

export const Navbar = () => {
  const navigate = useNavigate();
  const searchQuery = useRef();
  const handleKeyDown = (event) => {
    if (event.key === "Enter") {
      if(searchQuery.current.value.length <= 0){
        alert("Please enter something to search.")
      }else{
        navigate("/", {state: {query: searchQuery.current.value}});
        searchQuery.current.value = "";
      }
    }
  };

  return (
    <div className="navbar">
      <div className="input">
        <BiSearchAlt className="icon" />
        <input
          type="text"
          name="search"
          onKeyDown={handleKeyDown}
          placeholder="Search"
          id="search"
          ref={searchQuery}
        />
        <MdOutlineKeyboardVoice className="ic2" />
      </div>
      <div className="avatar">
        <img src={avatar} alt="Avatar" />
      </div>
    </div>
  );
};
