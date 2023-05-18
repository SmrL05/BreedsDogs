% rebase('layout.tpl', title=title, year=year)
<img src="/static/image/picArticle.jpg" height = 640 margin = 0px/>

<div class="row">
    <div class="col-md-12 gap-3 border-10 margin-top-0" id="block_background" style="height: 400px">
        <div class="jumbotron  text-center margin-5" id="block_background" style="height: 40px" >
            <h2  class="h">Add your article</h2>
        </div> 
        <form action="/article" method="post">
            <p><textarea required style="resize: none;" class="input" rows="3" cols="80" name="ARTICLE" placeholder="Your article"></textarea></p> 
            <p><input required type="text" class="input" size="50" name="NAME_AUTHOR" placeholder="Name of author"></p>
            <p><input required type="text" pattern="([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+$" class="input" size="50" name="EMAIL_AUTHOR" placeholder="Email of author"></p>
            <p><input required type="text" class="input" size="50" name="PHONE_AUTHOR" placeholder="Phone of author"></p>
            <p><input required type="submit" class="shine-button" value="Send"></p>
        </form>
    </div>   
 </div>