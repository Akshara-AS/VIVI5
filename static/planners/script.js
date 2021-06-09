var app = new Vue({
  el: "#app",
  data: {
    todos: [
      
    ],
    todo: "",
  },
  methods: {
    deleteItem: (item) => {
      let index = app.todos.indexOf(item);
      app.todos.splice(index, 1);
    },
    addItem: () => {
      if (app.todo) {
        app.todos.push({ id: app.todos.length, text: app.todo, isDone: false });
        app.todo = "";
      } else {
      }
    },
    toggleDone: (item) => {
      item.isDone = !item.isDone;
    },
  },
});
