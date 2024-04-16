# Nodejs development

In order to understand Node, you need to have all these in mind:

- Nodejs is a runtime environment for executing Javascript code
- Essentially, Node is a C++ program that embeds Chrome's V8 engine, the fastest Js engine in the world
- We use Node to build fast and scalable networking applications. It's a perfect choice for building RESTful services
- Node applications are single-threaded. That means a single thread is used to serve all clients.
- Node applications are asynchronous or non-blocking by default. That means when the application involves I/O operations (e.g accessing the file system or the network). the thread does not wait (or block) for the result of the operation. It is realeased to seve other clients.
- This architecture makes Node ideal for building I/O-intensive applications.
- You should avoid using Node for CPU-intensive applications, such as video encoding service. This is because while executing these operations, other clients have to wait for the single thread to finish its job and be ready to serve them.
- In Node, we don't have a web browser environment object such as window or the document object. Instead, we have other objects that are not available in the web browsers such as objects for working with the file system, network, operating system etc

