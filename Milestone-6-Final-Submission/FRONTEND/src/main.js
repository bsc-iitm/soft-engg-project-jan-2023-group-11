import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import axios from "axios";

axios.defaults.baseURL = "http://127.0.0.1:5001";
axios.defaults.headers.common["Access-Control-Allow-Origin"] = "*";

import "./assets/style.css";
import store from "./store";

const app = createApp(App).use(store);

app.use(router);

app.mount("#app");
