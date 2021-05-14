$(document).ready(function(){

    // State : after selection of country
    $("#country").change(function(){
        let country_name = $(this).val();
        $.ajax({
            url: `${state_data_url}?country_name=${country_name}`,
            type: 'get',
            dataType: 'json',

            success:function(response){
                response = JSON.parse(response);
                var len = response.length;

                $("#state").empty();
                $("#state").append('<option disabled="true" selected="true">--none--</option>')
                for( let i = 0; i<len; i++){
                    let state_name = response[i].fields.state_name;
                    $("#state").append("<option value='"+state_name+"'>"+state_name+"</option>");
                }
            }
        });
    });

    // District : after selection of state
    $("#state").change(function(){
        let state_name = $(this).val();
        $.ajax({
            url: `${district_data_url}?state_name=${state_name}`,
            type: 'get',
            dataType: 'json',

            success:function(response){
                response = JSON.parse(response);
                var len = response.length;

                $("#district").empty();
                $("#district").append('<option disabled="true" selected="true">--none--</option>')
                for( let i = 0; i<len; i++){
                    let district_name = response[i].fields.district_name;
                    $("#district").append("<option value='"+district_name+"'>"+district_name+"</option>");
                }
            }
        });
    });

    // District : after selection of state
    $("#district").change(function(){
        let district_name = $(this).val();
        $.ajax({
            url: `${city_data_url}?state_name=${district_name}`,
            type: 'get',
            dataType: 'json',

            success:function(response){
                response = JSON.parse(response);
                var len = response.length;

                $("#city").empty();
                $("#city").append('<option disabled="true" selected="true">--none--</option>')
                for( let i = 0; i<len; i++){
                    let city_name = response[i].fields.city_name;
                    $("#city").append("<option value='"+city_name+"'>"+city_name+"</option>");
                }
            }
        });
    });

});