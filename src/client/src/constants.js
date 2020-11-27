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
    text: "O(nlogn)",
    position: "INSIDE",
    color: "#555",
    fontSize: "19px",
  },
  {
    text: "O(n)",
    position: "INSIDE",
    color: "#555",
  },
  {
    text: "O(logn)",
    position: "INSIDE",
    color: "#555",
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

export const getFilteredInputData = (data, type) => {
  if (type === "e2e_runtime") {
    return data["e2e"][type].map((d) => {
      return { n: d["n"], total_runtime: d["total_runtime"] };
    });
  } else if (type === "e2e_memory") {
    return data["e2e"][type].map((d) => {
      return { n: d["n"], total_memory: d["total_memory"] };
    });
  }

  return [];
};
