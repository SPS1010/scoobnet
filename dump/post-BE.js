function createPost(postData) {
   const fs = require('fs');

   const huntId = 'hunt-' + Math.floor(Math.random() * 10000);
   
   const newHunt = {
       huntId: huntId,
       huntName: postData.huntName,
       huntActive: postData.huntActive,
       huntBanner: postData.huntBanner,
       huntOwner: 'Anonymous'
   };
   
   fs.appendFileSync('hunts.json', JSON.stringify(newHunt, null, 2));
}

document.getElementById('postForm').addEventListener('submit', function(event) {
   event.preventDefault();
   
   const postData = {
       huntName: document.getElementById('huntName').value,
       huntActive: document.getElementById('huntActive').checked,
       huntBanner: document.getElementById('huntBanner').value
   };
   
   createPost(postData);
   document.getElementById('postForm').reset();
});
