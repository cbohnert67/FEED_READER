###################################################################
#                                                                 #
#                          FeedReader App                         #
#                         
#                                                              #
#                         30/04/2022 v.0.1                        #
#                                                                 #
#                          Cédric Bohnert                         #
#                                                                 #
###################################################################

from rss.Feed import *
import click

@click.command()
@click.option('--top', default=0, help='Top N entries that should be displayed for a feed. Must be used with only one url.')
@click.option('--title', is_flag=True, help="Displays titles of all entries in each feed.")
@click.option('--all', is_flag=True, help="Displays all entries in each feed.")
@click.argument('urls', nargs=-1)
def feedreader(top, title, all, urls):
    """Simple feed reader that reads urls and displays feeds content."""
    
    if all:
        for url in urls:
           feed = Feed(url)
           for entry in feed.getEntries():
               click.echo(str(entry))
    elif title:
        for url in urls:
            feed = Feed(url)
            click.echo()
            click.echo(feed.getTitle().upper())
            click.echo()
            titles = ""
            for entry in feed.getEntries():
                titles += "- "
                titles += entry.getTitle()
                titles += "\n"
            click.echo(titles)
    elif top!=0:
        if len(urls)>1:
            click.echo("This option must be used with only one url.")
        else:
            if top<0:
                click.echo("Invalid option.")
            else:
                feed = Feed(urls[0])
                length = feed.getLength()
                if top>length:
                    click.echo("There are only {} entries :".format(length))
                    click.echo()
                    top = length
                for entry in feed.getEntries()[:top]:
                    click.echo(str(entry))
    else:
        for url in urls:
            click.echo(Feed(url).getInfo())

if __name__ == '__main__':
    feedreader()