import React, {Component} from "react";
import MainRoute from "./Routes/MainRoute";
import {withRouter} from 'react-router-dom';
import './asset/css/App.css';
import Navigation from "./Components/Navigation";

class AppAjax extends Component {
    postSignout = () => {
        localStorage.removeItem("is_login");
        this.props.history.push("/");
        };
        render() {
            return (
                <div>
                    <Navigation postSignout = {this.postSignout} />
                    <MainRoute />
                </div>
            );
        }
    }

export default withRouter(AppAjax);