const path = require('path');
const ExtractTextPlugin = require('extract-text-webpack-plugin');

module.exports = {
    entry: ['./assets/js/app.js', './assets/scss/main.scss'],
    output: {
        filename: 'js/bundle.js',
        path: path.resolve(__dirname, 'website/static/')
    },
    module: {
        rules: [{ // sass / scss loader for webpack
                test: /\.(sass|scss)$/,
                loader: ExtractTextPlugin.extract(['css-loader', 'sass-loader']),
            },
            {
                test: /\.(png|jpg|gif)$/,
                use: [{
                    loader: 'url-loader',
                }]
            },
            {
                test: /\.(ttf|eot|woff|woff2)$/,
                loader: "url-loader",
              },
        ]
    },
    plugins: [
        new ExtractTextPlugin({ // define where to save the file
            filename: './css/main.bundle.css',
            allChunks: true,
        }),
    ],
    // Automatically compile when files change.
    watch: true,
    // Automatically reload the page when compilation is done.

    devServer: {
        inline: true,
        //contentBase: 'http://127.0.0.1:8000',
        proxy: {
            "*": 'http://127.0.0.1:8000'
        }
        // proxy: [{
        //     target: 'http://127.0.0.1:8000',
        //     secure: false
        // }]
    },
};