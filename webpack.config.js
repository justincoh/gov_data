const webpack = require("webpack");
const path = require("path");

module.exports = {
    entry: ["./static/src/index.js"],
    output: {
        path: path.resolve(__dirname, "static/dist"),
        publicPath: path.resolve(__dirname, "static/dist"),
        filename: "bundle.js"
    },
    devServer: {
        contentBase: "static/dist"
    },
    module: {
        rules: [
        {
            test: /\.js$/,
            exclude: /node_modules/,
            use: {
            loader: "babel-loader"
            }
        }
        ]
    },
    resolve: {
        extensions: [".js"],
        modules: [
            path.resolve(__dirname, "./static/src"),
            "node_modules",
        ],
        // alias: {}
    },
    plugins: [
        new webpack.ProvidePlugin({
            React: 'react',
            ReactDOM: 'react-dom'
        }),
    ]
};