import data from "../../Data/data.json";

export const loadData = () => {
  return {
    type: "LOAD_DATA",
    data,
  };
};
