var path = require('path');
const HtmlWebPackPlugin = require("html-webpack-plugin");
module.exports ={

    entry: path.resolve(__dirname, './src'),
    output: {
        path: path.resolve(__dirname, '../main/flaskr/templates'),
        filename: "../static/main.js"
    },
    module:{
        rules: [
            {
                test: /\.(js|jsx)$/,
                exclude: /node_modules/,
                use:{
                    loader: "babel-loader"
                }
                
            },
            {
                test: /\.html$/,
                exclude: /node_modules/,
                use:{
                    loader: "html-loader"
                }
            }
        ]
    },
    plugins: [
        new HtmlWebPackPlugin({
            template: "src/index.html",
            filename: "./index.html"
        })
    ]
}