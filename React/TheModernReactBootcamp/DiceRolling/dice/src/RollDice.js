import React, { useState } from "react";
import Die from "./Die";
import "./RollDice.css";

const RollDice = () => {
  const sides = ["one", "two", "three", "four", "five", "six"];

  const [die, setDie] = useState({ die1: "one", die2: "one", rolling: false });

  const roll = () => {
    //pick 2 new rolls
    const newDie1 = sides[Math.floor(Math.random() * sides.length)];
    const newDie2 = sides[Math.floor(Math.random() * sides.length)];
    //set state with new rolls
    setDie({
      die1: newDie1,
      die2: newDie2,
      rolling: true,
    });

    //wait one second, then set rolling to false
    setTimeout(() => {
      setDie({ die1: newDie1, die2: newDie2, rolling: false });
    }, 1000);
  };

  return (
    <div className="RollDice">
      <div className="RollDice-container">
        <Die face={die.die1} rolling={die.rolling} />
        <Die face={die.die2} rolling={die.rolling} />
      </div>
      <button onClick={roll} disabled={die.rolling}>
        {die.rolling ? "Rolling..." : "Roll Dice!"}
      </button>
    </div>
  );
};

export default RollDice;
