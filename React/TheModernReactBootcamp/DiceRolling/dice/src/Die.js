import React from "react";
import "./Die.css";

const Die = ({ face, rolling }) => {
  return <i className={`Die fas fa-dice-${face} ${rolling && "shaking"}`}></i>;
};

export default Die;
