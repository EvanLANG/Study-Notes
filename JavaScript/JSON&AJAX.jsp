<script>
        function loadDoc() {
            var xhttp = new XMLHttpRequest();
            xhttp.onreadystatechange = function() {
                if (this.readyState == 4 && this.status == 200) {
                    var obj = JSON.parse(this.responseText);
                    var item = obj.results;
                    myFunction(item);
                }
            };
            xhttp.open("GET", "https://api.nytimes.com/svc/mostpopular/v2/mostviewed/Business%20Day/1.json?api-key=e716033797834288814805dc70eb4907", true);
            xhttp.send();
        }
        function myFunction(x) {
            var num = 0;
            var i;
            // there is somthing need to be fixed, index should start from 1
            var out="";
            var max = Math.min(10,x.length);
            for (i = 0; i < max; i++) {
                if(x[i].media[0]['media-metadata'][2]!=null||typeof(x[i].media[0]['media-metadata'][2])!='undefined'){
                    out += '<p><span><a href="' + x[i].url + '"target="_blank">' + x[i].title + "</a></span><br><img src="+ x[i].media[0]['media-metadata'][2].url +'><br><span class="small">'+x[i].abstract+'</span><br><span class="small">'+x[i].byline+'&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp'+x[i].published_date+'</span><br><br>';
                }else{
                    out += '<p><span><a href="' + x[i].url + '"target="_blank">' + x[i].title + '</a></span><br><span class="small">'+x[i].abstract+'</span><br><span class="small">'+x[i].byline+'&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp'+x[i].published_date+'</span><br><br>';
                }
            }
            document.getElementById("comment").innerHTML=out;
        }
    </script>
