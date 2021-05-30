cli2の設定
vue init webpack clinent
jest.config.jsに以下を追記
    module.exports = {
    ...
    verbose: true,
    testURL: "http://localhost/",
    }


cli3の設定
vue create {project_name}
vue add router
vue add @vue/eslint
vue add unit-jest


publicに置いてから、/test.png 的な感じで指定


npm install axios
で、import axios from "axios";