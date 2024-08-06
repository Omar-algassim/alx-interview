#!/usr/bin/node
const request = require('request')

const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}/`;


request.get(url, function (error, response) {
    if (error) {
    console.error(error);
    }else {
        const data = JSON.parse(response.body)["characters"]
        data.forEach(link => {
            request.get(link, function(error, response) {
                if (error) {
                    console.error(error)
                }else {
                    const film_info = JSON.parse(response.body);
                    console.log(film_info['name'])
                }
            })
            
        });
    }
})