import React from "react";
import {Route, Switch} from "react-router-dom";
import Home from "../Components/Home";
import SignIn from "../Components/SignIn";
import SignUp from "../Components/SignUp";
import NotMatch from "../Components/NotMatch";
import News_1 from "../Components/News_1";
import Profile from "../Components/Profile";

const MainRoute = () => {
    return (
        <Switch>
            <Route exact path="/" component={Home} />
            <Route exact path="/signin" component={SignIn} />
            <Route exact path="/signup" component={SignUp} />
            <Route exact path="/profile" component={Profile} />
            {/* <Route exact path="/news" component={News_1} /> */}
            <Route component={NotMatch} />        
        </Switch>
    );
};

export default MainRoute;