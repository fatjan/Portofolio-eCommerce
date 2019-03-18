import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import * as serviceWorker from './serviceWorker';
import AppRouter from "./AppRouter";
import { BrowserRouter } from 'react-router-dom';
import {Provider} from 'unistore/react';
import {store} from "./Components/store";

ReactDOM.render(<App />, document.getElementById('root'));
const render = Component =>
ReactDOM.render(
    <Provider store={store} >
        <BrowserRouter>
            <Component />
        </BrowserRouter>
    </Provider>,
    rootEl
);

render (AppRouter);

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.register();
