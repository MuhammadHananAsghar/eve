import React from "react";
import { Navbar } from "./Navbar";
import { Sidebar } from "./Sidebar";
import { Main } from "./Main";
import { Player } from './Player';
import {
  BrowserRouter as Router,
  Routes,
  Route,
} from "react-router-dom";
import { Navigate } from "react-router-dom";

import "../styles/App.css";

const App = () => {
  return (
    <div className="app">
      <Router>
        <Sidebar />
        <Navbar />
        <Routes>
          <Route exact path="/" element={<Main />} />
          <Route exact path="/player" element={<Navigate to="/" />} ></Route>
          <Route path="/player/:title/:id" element={<Player />} ></Route>
        </Routes>
      </Router>
    </div>
  );
};

export default App;
