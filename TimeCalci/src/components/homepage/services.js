
export default class SearchService{

    constructor(){

    }

    searchByName(callHistoryArr, name){
        name=name.toLowerCase();
        let result = new Array();
        callHistoryArr.forEach(element => {
            if(element.name!=null){
                if(element.name.toLowerCase().search(name)>=0){
                    result.push(element);
                }
            }
        });
        return result;
    }

    searchByNumber(callHistoryArr, number){
        let result = new Array();
        callHistoryArr.forEach(element => {
            if(element.phoneNumber.search(number)>=0){
                result.push(element);
            }
        });
        return result;
    }
}