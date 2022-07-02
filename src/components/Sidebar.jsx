import React, { useState } from "react";
import "../styles/Sidebar.css";
import {
  RiMovie2Line,
  RiHome7Fill,
  RiCompassDiscoverFill,
} from "react-icons/ri";
import { FiSettings } from "react-icons/fi";
import { useNavigate } from "react-router-dom";

export const Sidebar = () => {
  const [activeId, setActiveId] = useState(1);
  const navigate = useNavigate();
  const [sidbarStyle, setSidebarStyle] = useState({
    position: "relative",
    top: "0",
    left: "-280px",
  });

  const values = [
    { id: 1, text: "Home", icon: <RiHome7Fill className="icon" /> },
    {
      id: 2,
      text: "Discover",
      icon: <RiCompassDiscoverFill className="icon" />,
    },
    { id: 3, text: "Movies", icon: <RiMovie2Line className="icon" /> },
    { id: 4, text: "GTA V" },
    { id: 5, text: "PUBG" },
    { id: 6, text: "CS GO" },
    { id: 7, text: "Settings", icon: <FiSettings className="icon" /> },
  ];

  const Spacer = () => {
    return <div className="iconDiv"></div>;
  };

  const sidebar = () => {
    if (sidbarStyle.left === "-280px") {
      setSidebarStyle({ position: "relative", top: "0", left: "0" });
    } else {
      setSidebarStyle({ position: "relative", top: "0", left: "-280px" });
    }
  };

  const handleClick = (id, text) => {
    setActiveId(id);
    if (text === "GTA V") {
      navigate("/", { state: { query: "gta five gameplays" } });
    } else {
      navigate("/", { state: { query: text } });
    }
  };

  return (
    <div className="sidebar" style={sidbarStyle}>
      <div className="logo" onClick={() => sidebar()}>
        <span className="lName">eve</span>
      </div>
      <div className="body">
        <ul>
          {values.map((val) => (
            <li
              className={activeId === val.id ? "activeLI" : "inactiveLI"}
              onClick={() => handleClick(val.id, val.text)}
            >
              {val.icon ? val.icon : <Spacer />}
              <span>{val.text}</span>
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
};
