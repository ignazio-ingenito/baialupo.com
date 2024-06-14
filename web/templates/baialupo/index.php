<?php

/**
 * Date         11-06-2013
 * Copyright    Copyright (C) 2013 Ignazio Ingenito
 * License  GPL
 */
defined('_JEXEC') or die;
$app = JFactory::getApplication();
$leftbar = 1;
$rightbar = 1;
?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="https://www.w3.org/1999/xhtml" xml:lang="<?php echo $this->language; ?>" lang="<?php echo $this->language; ?>">

<head>
  <meta name="google-site-verification" content="q794lHBh_br9CPhu3nU3QUUt3Rng0bSwg1NYTl9sc2U" />

  <jdoc:include type="head" />
  <script src="myAddon/jquery.bpopup.min.js" type="text/javascript"></script>

  <!-- jquery -->
  <link rel="stylesheet" href="https://code.jquery.com/ui/1.11.4/themes/ui-lightness/jquery-ui.css">
  <script src="https://code.jquery.com/ui/1.11.4/jquery-ui.js"></script>
  <!-- fine jquery -->

  <!-- google fonts -->
  <!-- fine google fonts -->

  <link rel="stylesheet" href="<?php echo $this->baseurl ?>/templates/system/css/system.css" type="text/css" />
  <link rel="stylesheet" href="<?php echo $this->baseurl ?>/templates/system/css/general.css" type="text/css" />
  <link rel="stylesheet" href="<?php echo $this->baseurl ?>/templates/<?php echo $this->template ?>/css/template.css" type="text/css" />
  <link href='https://fonts.googleapis.com/css?family=Open+Sans:400,300,600,700' rel='stylesheet' type='text/css'>
  <link href='https://fonts.googleapis.com/css?family=Lato:300,400,700' rel='stylesheet' type='text/css'>
  <link href='https://fonts.googleapis.com/css?family=Open+Sans+Condensed:300' rel='stylesheet' type='text/css'>
  <link href='https://fonts.googleapis.com/css?family=Alegreya+Sans+SC:900' rel='stylesheet' type='text/css'>
  <script src="<?php echo $this->baseurl ?>/templates/<?php echo $this->template ?>/js/baia.js" type="text/javascript"></script>

  <!-- Tailwind.css -->
  <script src="https://cdn.tailwindcss.com"></script>

  <!-- Begin Cookie Consent plugin by Silktide - http://silktide.com/cookieconsent -->
  <script type="text/javascript">
    window.cookieconsent_options = {
      "message": "Il nostro sito utilizza cookie tecnici e, previo tuo consenso, cookie di profilazione, nostri e di terze parti. Se vuoi saperne di più o prestare il consenso solo ad alcuni utilizzi",
      "dismiss": "Ok",
      "learnMore": "clicca qui.",
      "link": "<?php echo $this->baseurl ?>/195-cookie-policy",
      "theme": "dark-top"
    };
  </script>
  <script type="text/javascript" src="//s3.amazonaws.com/cc.silktide.com/cookieconsent.latest.min.js"></script>
  <!-- End Cookie Consent plugin -->
  <?php
  if ($this->countModules('left') == 0)
    $leftbar    = "0";

  if ($this->countModules('right') == 0)
    $rightbar   = "0";
  ?>
</head>

<body id="page_bg">
  <!-- Google Analytics -->
  <script>
    (function(i, s, o, g, r, a, m) {
      i['GoogleAnalyticsObject'] = r;
      i[r] = i[r] || function() {
        (i[r].q = i[r].q || []).push(arguments)
      }, i[r].l = 1 * new Date();
      a = s.createElement(o),
        m = s.getElementsByTagName(o)[0];
      a.async = 1;
      a.src = g;
      m.parentNode.insertBefore(a, m)
    })(window, document, 'script', '//www.google-analytics.com/analytics.js', 'ga');

    ga('create', 'UA-44786164-1', 'baialupo.com');
    ga('set', 'anonymizeIp', true);
    ga('send', 'pageview');
  </script>
  <!-- Fine Google Analytics -->

  <div id="bg">
    <div id="top_bg">
      <div id="footer_bg">
        <div id="container">

          <div id="top">
            <div id="pillmenu">
              <jdoc:include type="modules" name="top" style="xhtml" />
            </div>
            <div id="search">
              <jdoc:include type="modules" name="search" style="xhtml" />
            </div>
            <div class="clr"></div>
          </div>

          <div id="header">
            <div id="header_l">
              <div id="header_r">
                <div id="header_img">
                  <jdoc:include type="modules" name="slider" style="xhtml" />
                </div>
                <div class="cpathway">
                  <jdoc:include type="modules" name="breadcrumbs" style="xhtml" />
                </div>
              </div>
            </div>
          </div>

          <div id="content_bottom">
            <div id="content">
              <?php if ($this->countModules('left')) : ?>
                <div id="leftcolumn">
                  <jdoc:include type="modules" name="left" style="xhtml" />
                </div>
              <?php endif; ?>

              <div id="maincolumn_left">
                <div class="nopad">
                  <jdoc:include type="message" />
                  <jdoc:include type="component" />
                </div>
              </div>


              <div class="clr"></div>
            </div>
          </div>
          <div id="footer">
            <jdoc:include type="modules" name="footer" style="xhtml" />
          </div>
        </div>
      </div>
    </div>
  </div>
  <jdoc:include type="modules" name="debug" />
</body>

</html>