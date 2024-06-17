---
id: 141
title: Webcam
alias: webcam
category: baialupo
featured: 0
created: 2012-11-17T23:00:00
updated: 2017-10-26T15:41:08
created_by: ignazio
---
<p style="text-align: center;">
 <a href="#" name="fullview" target="_blank">
  <img border="0" name="webcam" src="images/ajax-loader.gif"/>
 </a>
 <br/>
 <br/>
 <a href="#" name="fullview" target="_blank">
  Clicca per vedere a schermo pieno
 </a>
</p>
<script type="text/javascript">
 // <![CDATA[
$(function() {
   var url1 = "http://95.243.125.41:8089/cgi-bin/image.cgi?userName=webcam&password=Webc@m12654&cameraID=1&quality=4";
   var url2 = "http://95.243.125.41:8089/cgi-bin/image.cgi?userName=webcam&password=Webc@m12654&cameraID=1&quality=9";

   $("img[name='webcam']").attr("src", url1);
   $("a[name='fullview']").attr("href", url2);
   $("img[name='webcam']").bind('load', function() {
      $(this).attr("width", "100%");
   });
});
// ]]>
</script>
