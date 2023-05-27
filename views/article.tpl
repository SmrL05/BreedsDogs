% rebase('layout.tpl', title=title, year=year, error=error)
<img src="/static/image/picArticle.jpg" height = 640 margin = 0px/>

<div class="row">
    <div class="col-md-12 gap-3 border-10 margin-top-0" id="block_background" style="height: 400px">
        <div class="jumbotron  text-center margin-5" id="block_background" style="height: 40px" >
            <h2 class="h p-20">Add your article</h2>
        </div> 
        <form action="/article" method="post">
            <div class="row p-20">
                <div class="col-md-3 col-md-offset-0 border-10" style="margin: 2px 45px 2px 230px;">
                    <p><input required type="text" class="input" size="50" name="URL_ARTICLE" placeholder="Link to your article"></p>
                    <p><textarea required style="resize: none;" class="input" rows="7" cols="80" name="ARTICLE" placeholder="Abstract for your article"></textarea></p> 
                </div>   
                <div class="col-md-3 col-md-offset-0 border-10" style="margin: 2px 180px 2px 45px;">
                    <p><input required type="text" class="input" size="50" name="NAME_AUTHOR" placeholder="Name of author"></p>
                    <p><input required type="text" pattern="([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+$" class="input" size="50" name="EMAIL_AUTHOR" placeholder="Email of author"></p>
                    <p><input required type="text" class="input" size="50" name="PHONE_AUTHOR" placeholder="Phone of author"></p>
                    <p><input required type="submit" class="shine-button" value="Send"></p>
                </div>   
                <div class="col-md-12 col-md-offset-0">
                    <h3 class = "erorrtext_ flex-center-col"><b>{{error</b></h3>
                </div>
            </div>   
        </form>
    </div>   
 </div>