document.getElementById('postPost').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const postData = {
        huntName: document.getElementById('huntName').value,
        huntActive: document.getElementById('huntActive').checked,
        huntBanner: document.getElementById('huntBanner').value
    };
    
    createPost(postData);
    document.getElementById('postPost').reset();
});
