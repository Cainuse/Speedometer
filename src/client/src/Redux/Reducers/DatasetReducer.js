const initialState = {
  e2e: {
    e2e_runtime: [],
    e2e_memory: [],
  },
};

const DatasetReducer = (state = initialState, action) => {
  switch (action.type) {
    case "LOAD_DATA":
      return action.data;
    default:
      return state;
  }
};

export default DatasetReducer;
