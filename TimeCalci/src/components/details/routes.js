import Daily from './daily';
import Week from './week';
import Month from './month';
import Year from './year';

const DailyRoute = (allCallsArray) => (
    <Daily filteredCallHistoryArr={allCallsArray} />
);

const WeekRoute = (allCallsArray) => (
    <Week filteredCallHistoryArr={allCallsArray} />
);

const MonthRoute = (allCallsArray) => (
    <Month filteredCallHistoryArr={allCallsArray} />
);

const YearRoute = (allCallsArray) => (
    <Year filteredCallHistoryArr={allCallsArray} />
);

const routesKeyTitle = [
    { key: 'daily', title: 'daily' },
    { key: 'week', title: 'Week' },
    { key: 'month', title: 'Month' },
    { key: 'year', title: 'Year' },
]

export { routesKeyTitle, DailyRoute, WeekRoute, MonthRoute, YearRoute}