import React from "react";
import { createStore } from "redux";
import ReactDOM from "react-dom";
import { Provider } from "react-redux";
import "./index.css";
import App from "./App";
import rootReducer from "./Redux/Reducers/RootReducer";
import { loadData } from "./Redux/Actions/DatasetActions";

const store = createStore(rootReducer);

// Populate the store with data received from the execution of py script
store.dispatch(loadData());

ReactDOM.render(
  <React.StrictMode>
    <Provider store={store}>
      <App />
    </Provider>
  </React.StrictMode>,
  document.getElementById("root")
);
