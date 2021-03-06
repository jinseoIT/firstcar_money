document.cookie = "safeCookie1=foo; SameSite=Lax"; document.cookie = "safeCookie2=foo"; document.cookie = "crossCookie=bar; SameSite=None; Secure";

// 2. This code loads the IFrame Player API code asynchronously.
 var tag = document.createElement('script');

 tag.src = "https://www.youtube.com/iframe_api";
 var firstScriptTag = document.getElementsByTagName('script')[0];
 firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

 // 3. This function creates an <iframe> (and YouTube player)
 //    after the API code downloads.
function onYouTubeIframeAPIReady() {
   // <div id="player"></div>
   new YT.Player('player', {
     videoId: 'OpDZJRJ6W1Y', // 최초 재생할 유튜브 영상 ID
     playerVars: {
       autoplay: true,  // 자동 재생 유무
       loop: true, // 반복 재생 유무
        mute: 1,
       playlist: 'OpDZJRJ6W1Y' // 반복 재생할 유튜브 영상 ID목록
     },
     events: {
       onReady: function (event) {
         event.target.mute() // 음소거
       }
     }
   });
}
 
