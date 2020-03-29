import React, {Component} from 'react';
import { View, Text, StyleSheet, Dimensions } from 'react-native';
import { TabView, SceneMap, TabViewPage, TabViewAnimated } from 'react-native-tab-view';
import Day from './day';
import Week from './week';
import Month from './month';
import Year from './year';

const DayRoute = (data) => (
    <Day name={data.name} phoneNumber={data.phoneNumber} allCallsArray={data.allCallsArray} />
);

const WeekRoute = (data) => (
    <Week name={data.name} phoneNumber={data.phoneNumber} allCallsArray={data.allCallsArray} />
);

const MonthRoute = (data) => (
    <Month name={data.name} phoneNumber={data.phoneNumber} allCallsArray={data.allCallsArray} />
);

const YearRoute = (data) => (
    <Year name={data.name} phoneNumber={data.phoneNumber} allCallsArray={data.allCallsArray} />
);

const routesKeyTitle = [
    { key: 'daily', title: 'daily' },
    { key: 'week', title: 'Week' },
    { key: 'month', title: 'Month' },
    { key: 'year', title: 'Year' },
]

export default class Details extends Component {
    
    state = {
        tabIndex: 0,
        allCallsArray: null,
        routes: {}
    };

    constructor(props) {
        super(props);
        
        this.state.allCallsArray = props.route.params.allCallsArray;
        let data = {
            name: props.route.params.name,
            phoneNumber: props.route.params.phoneNumber,
            allCallsArray: props.route.params.allCallsArray
        };
        this.state.routes = {
            daily: DayRoute(data),
            week: WeekRoute(data),
            month: MonthRoute(data),
            year: YearRoute(data),
        }
        
    }

    onTabChange(index){
        this.setState({tabIndex:index});
    }

    getNavigationState(index){
        return {
            index: this.state.tabIndex,
            routes: routesKeyTitle
            
        }
    }

    _renderScene = ({ route }) => {
        switch (route.key) {
        case 'daily':
            return this.state.routes.daily;
        case 'week':
            return this.state.routes.week;
        case 'month':
            return this.state.routes.month;
        case 'year':
            return this.state.routes.year;
        default:
          return null;
        }
      };

    
    render(){
        return (
            <TabView
              navigationState={this.getNavigationState()}
              renderScene={this._renderScene}
              onIndexChange={(index) => this.onTabChange(index)}
            />
          );
    }
}

