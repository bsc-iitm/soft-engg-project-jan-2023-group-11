import { createStore } from "vuex";

export default createStore({
  state: {
    queries: [],
    selectedQuery: {},
    anonouncementModal: false,
    createPostModal: false,
    replyPostModal: false,
  },
  getters: {
    getQueries: (state) => {
      return state.queries;
    },
    getSelectedQueries: (state) => {
      return state.selectedQuery;
    },
    getannoucementModal: (state) => {
      return state.anonouncementModal;
    },
    getCreatePostModal: (state) => {
      return state.createPostModal;
    },
    getreplyPostModal: (state) => {
      return state.replyPostModal;
    },
  },
  mutations: {},
  actions: {},
  modules: {},
});
