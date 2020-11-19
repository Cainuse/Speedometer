export const LABELS = [
  {
    text: "O(n\u207F)",
    position: "INSIDE",
    color: "#555",
  },
  {
    text: "O(n!)",
    position: "INSIDE",
    color: "#555",
  },
  {
    text: "O(n\u00B3)",
    position: "INSIDE",
    color: "#555",
    fontSize: "19px",
  },
  {
    text: "O(n\u00B2)",
    position: "INSIDE",
    color: "#555",
  },
  {
    text: "O(n)",
    position: "INSIDE",
    color: "#555",
  },
  {
    text: "O(nlog(n))",
    position: "INSIDE",
    color: "#555",
    fontSize: "19px",
  },
  {
    text: "O(1)",
    position: "INSIDE",
    color: "#555",
    fontSize: "19px",
  },
];

export const getRandomColor = () => {
  var letters = "0123456789ABCDEF";
  var color = "#";
  for (var i = 0; i < 6; i++) {
    color += letters[Math.floor(Math.random() * 16)];
  }
  return color;
};
