dating-server:
	$(TROUPE)/bin/troupec dating-server.trp -o ./out/dating-server.js
	node $(TROUPE)/rt/built/troupe.js -f=./out/dating-server.js --id=../ids/id-server.json --trustmap=../trustmaps/GoT.json --aliases=aliases.json

dating-client1:
	$(TROUPE)/bin/troupec dating-client1.trp -o ./out/dating-client1.js
	node $(TROUPE)/rt/built/troupe.js -f=./out/dating-client1.js --id=../ids/id1-client.json --trustmap=../trustmaps/server.json

dating-client2:
	$(TROUPE)/bin/troupec dating-client2.trp -o ./out/dating-client2.js
	node $(TROUPE)/rt/built/troupe.js -f=./out/dating-client2.js --id=../ids/id2-client.json --trustmap=../trustmaps/server.json

dating-mal1:
	$(TROUPE)/bin/troupec dating-mal1.trp -o ./out/dating-mal1.js
	node $(TROUPE)/rt/built/troupe.js -f=./out/dating-mal1.js --id=../ids/id-mal1.json --trustmap=../trustmaps/server.json

dating-mal2:
	$(TROUPE)/bin/troupec dating-mal2.trp -o ./out/dating-mal2.js
	node $(TROUPE)/rt/built/troupe.js -f=./out/dating-mal2.js --id=../ids/id-mal2.json --trustmap=../trustmaps/server.json

dating-mal3:
	$(TROUPE)/bin/troupec dating-mal3.trp -o ./out/dating-mal3.js
	node $(TROUPE)/rt/built/troupe.js -f=./out/dating-mal3.js --id=../ids/id-mal3.json --trustmap=../trustmaps/server.json

dating-mal3helper:
	$(TROUPE)/bin/troupec dating-mal3helper.trp -o ./out/dating-mal3helper.js
	node $(TROUPE)/rt/built/troupe.js -f=./out/dating-mal3helper.js --id=../ids/id-mal3helper.json --trustmap=../trustmaps/server.json

