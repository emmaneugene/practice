import { useState } from "react";

const Game = () => {
  const [history, setHistory] = useState([Array(9).fill(null)]);
  const [currentMove, setCurrentMove] = useState(0);
  const putX = currentMove % 2 === 0;
  const grid = history[currentMove];

  const handlePlay = (nextSquares) => {
    const newHistory = [...history.slice(0, currentMove + 1), nextSquares];
    setHistory(newHistory);
    setCurrentMove(newHistory.length - 1);
  };

  const gotoMove = (idx) => {
    setCurrentMove(idx);
  };

  const moves = history.map((_, idx) => {
    let desc = idx > 0 ? `Go to move #${idx}` : "Go to game start";

    return (
      <li key={idx}>
        <button onClick={() => gotoMove(idx)}>{desc}</button>
      </li>
    );
  });

  return (
    <div className="game">
      <div className="game-board">
        <Board putX={putX} grid={grid} onPlay={handlePlay} />
      </div>
      <div className="game-info">
        <ol>{moves}</ol>
      </div>
    </div>
  );
};

const Board = ({ putX, grid, onPlay }) => {
  function handleClick(i) {
    if (grid[i]) {
      alert("Cell is already occupied");
      return;
    }

    if (calculateWinner(grid)) {
      return;
    }

    const nextSquares = grid.slice();
    nextSquares[i] = putX ? "X" : "O";
    onPlay(nextSquares);
  }

  const winner = calculateWinner(grid);
  let nextPlayer = putX ? "X" : "O";
  let status = winner ? `Winner: ${winner}` : `Next player: ${nextPlayer}`;

  return (
    <>
      <div className="status">{status}</div>
      <div className="board-row">
        <Square val={grid[0]} onClick={() => handleClick(0)} />
        <Square val={grid[1]} onClick={() => handleClick(1)} />
        <Square val={grid[2]} onClick={() => handleClick(2)} />
      </div>
      <div className="board-row">
        <Square val={grid[3]} onClick={() => handleClick(3)} />
        <Square val={grid[4]} onClick={() => handleClick(4)} />
        <Square val={grid[5]} onClick={() => handleClick(5)} />
      </div>
      <div className="board-row">
        <Square val={grid[6]} onClick={() => handleClick(6)} />
        <Square val={grid[7]} onClick={() => handleClick(7)} />
        <Square val={grid[8]} onClick={() => handleClick(8)} />
      </div>
    </>
  );
};

const Square = ({ val, onClick }) => {
  return (
    <button className="square" onClick={onClick}>
      {val}
    </button>
  );
};

const calculateWinner = (squares) => {
  const lines = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6],
  ];

  for (let i = 0; i < lines.length; i++) {
    const [a, b, c] = lines[i];
    if (squares[a] && squares[a] === squares[b] && squares[a] === squares[c]) {
      return squares[a];
    }
  }
  return null;
};

export default Game;
