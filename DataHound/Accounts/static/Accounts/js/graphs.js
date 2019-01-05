{% load staticfiles %}

d3.csv("media/bodata.csv").get(function(error,data){
    console.log(data);

})
