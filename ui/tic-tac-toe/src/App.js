import { useState } from "react";

const Square = ({ val, onClick }) => {

  return (
    <button
      className="square"
      onClick={onClick}
    >
      {val}
    </button>
  );
}

const calculateWinner = (squares) => {
  const lines = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
  ];

  for (let i = 0; i < lines.length; i++) {
    const [a, b, c] = lines[i];
    if (squares[a] && squares[a] === squares[b] && squares[a] === squares[c]) {
      return squares[a];
    }
  }
  return null;
}

const Board = () => {
  const [putX, setPutX] = useState(true);
  const [squares, setSquares] = useState(Array(9).fill(null));

  function handleClick(i) {
    if (squares[i]) {
      alert("Cell is already occupied");
      return;
    }

    if (calculateWinner(squares)) {
      return;
    }

    const nextSquares = squares.slice();
    nextSquares[i] = putX ? "X" : "O";
    setSquares(nextSquares);
    setPutX(!putX)

  }

  const winner = calculateWinner(squares);
  let nextPlayer = putX ? "X" : "O"
  let status = winner ? `Winner: ${winner}` : `Next player: ${nextPlayer}`

  return (
    <>
      <div className="status">{status}</div>
      <div className="board-row">
        <Square val={squares[0]} onClick={() => handleClick(0)} />
        <Square val={squares[1]} onClick={() => handleClick(1)} />
        <Square val={squares[2]} onClick={() => handleClick(2)} />
      </div>
      <div className="board-row">
        <Square val={squares[3]} onClick={() => handleClick(3)} />
        <Square val={squares[4]} onClick={() => handleClick(4)} />
        <Square val={squares[5]} onClick={() => handleClick(5)} />
      </div>
      <div className="board-row">
        <Square val={squares[6]} onClick={() => handleClick(6)} />
        <Square val={squares[7]} onClick={() => handleClick(7)} />
        <Square val={squares[8]} onClick={() => handleClick(8)} />
      </div>
    </>
  );
}

export default Board;
