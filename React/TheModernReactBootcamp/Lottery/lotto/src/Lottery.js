import React, { useState } from "react";
import Ball from "./Ball";
import "./Lottery.css";

const Lottery = ({ title, numBalls, maxNum }) => {
  const [nums, setNums] = useState(Array.from({ length: numBalls }));

  const generate = () => {
    setNums(nums.map((n) => Math.floor(Math.random() * maxNum) + 1));
  };

  return (
    <section className="Lottery">
      <h1>{title}</h1>
      <div>
        {nums.map((n) => (
          <Ball num={n} />
        ))}
      </div>
      <button onClick={generate}>Generate</button>
    </section>
  );
};

export default Lottery;
