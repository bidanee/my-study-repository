const {createServer} = require('node:http');

const hostname = '127.0.0.1';
const port = 3000;

const server = createServer((req,res) => {
	res.statusCode = 200;
    res.setHeader('Content-Type', 'text/plain; charset=utf-8');
    res.end('이게 바로 제 서버입니다만')
})

server.listen(port, hostname, () => {
	console.log('나도 이제 node.js로 서버개발 가능?')
})