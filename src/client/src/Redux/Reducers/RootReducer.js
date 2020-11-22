import { combineReducers } from "redux";
import datasetReducer from "./DatasetReducer";

const rootReducer = combineReducers({
  dataset: datasetReducer,
});

export default rootReducer;
