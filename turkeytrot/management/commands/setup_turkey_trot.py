from django.core.management.base import BaseCommand
from wagtail.models import Site, Page
from turkeytrot.models import TurkeyTrotPage
from datetime import datetime


class Command(BaseCommand):
    help = "Set up initial Turkey Trot page with content"

    def handle(self, *args, **options):
        # Get the root page
        root_page = Page.objects.get(slug="root")

        # Check if page already exists
        if TurkeyTrotPage.objects.filter(slug="turkey-trot-2025").exists():
            self.stdout.write(self.style.WARNING("Turkey Trot page already exists!"))
            return

        # Create Turkey Trot page
        turkey_trot_page = TurkeyTrotPage(
            title="Roadtown Turkey Trot 2025",
            slug="turkey-trot-2025",
            live=True,
            title_override="Roadtown Turkey Trot 2025",
            event_date=datetime(2025, 11, 22, 9, 0),
            event_location="Shutesbury Elementary",
            event_address="23 West Pelham Rd, Shutesbury, MA 01072",
            donate_url="https://www.paypal.com/donate/?cmd=_s-xclick&hosted_button_id=7DXZDF7XA5UQN&ssrt=1749578781197",
            registration_url="",
            # sponsor_packet_pdf will be uploaded through admin
            volunteer_url="",
            results_url="",
            photos_url="",
            about_event="<p>On a crisp autumn morning, runners and walkers of all ages and abilities will gather at the heart of Shutesbury for an invigorating 5K road race. The course will wind through the picturesque roads, providing a scenic backdrop as participants stride towards the finish line. Whether you're an avid runner seeking a new challenge or a walking enthusiast looking for a fun activity to kickstart your Thanksgiving celebrations, the Turkey Trot promises to be an event for everyone. The Event will:</p><ul><li>Feature a kids' run.</li><li>Have prizes to fill your Thanksgiving tables.</li><li>Showcase local business sponsors.</li><li>Raise funds for a new Shutesbury library.</li></ul>",
            route_description="<p>Beginning on Leverett Road, this course will take you through both the paved and dirt roads of hilly Shutesbury. The course ends on a big down hill at the Shutesbury Elementary School.</p>",
            parking_info="<p>Parking is at Shutesbury Elementary School, 23 West Pelham Road. The start line is an easy quarter mile walk up the road.</p>",
            sponsor_description='<p>This event is a fun and meaningful way to connect with the community while supporting a great cause. All proceeds benefit the new library, which is the culmination of years of hard work and generosity. Become a sponsor in just three easy steps:</p><ol><li>Choose a Sponsorship Level from our Sponsorship Packet (upload the PDF document through the admin).</li><li>Fill out a Sponsorship form <a href="https://docs.google.com/forms/d/e/1FAIpQLSfzCxvOBRzuc2C5ao8zRUYjAgoH2BmNoWHh1DKNNRrshALqVw/viewform?usp=dialog" target="_blank">here</a>.</li><li>Mail a check made out to FSML to P.O. Box 256, Shutesbury, MA 01072 or pay online via PayPal <a href="https://www.paypal.com/donate/?cmd=_s-xclick&hosted_button_id=7DXZDF7XA5UQN&ssrt=1749578781197" target="_blank">here</a>.</li></ol>',
            about_us="<p>Built in 1902, the M.N. Spear Memorial Library is a single 900 sq ft room with no running water. We love our current library and it has served us well for the past 120+ years, but we have outgrown it. Today libraries are so much more than repositories for books. Libraries offer videos and audio books, computers, museum passes, science kits, and spaces for people to meet and work together. While we have managed to meet some of these needs, the current space is woefully inadequate.</p><p>Our Library is the heart of our community, offering programs for everyone – from story time for our youngest visitors to fitness classes for seniors – and providing opportunities for community connections for all. We need a need a bigger library for all of this, plus, we would like to wash our hands after using a bathroom.</p><p>In 2022 we became the fortunate recipients of the one and only Massachusetts Small Library Pilot Grant, which will cover 75% of the cost of a new library. Most importantly, 83% of voters supported moving forward with the grant. We are designing our new library now and will break ground in Spring of 2024.</p><p>The Friends of the MN Spear Memorial Library have anticipated this moment and have worked hard since 2010 to raise funds for our Town's share of a new library. We have a goal of $550,000 by the time we break ground next spring. We now have $460,000, all raised from within our small community of just under 1,800 residents. For ten years we've hosted bake sales and tag sales, collected deposit recyclables and organized Giving Day appeals. We are now looking to our broader community to help us clear the last hurdle. At this time of Thanksgiving, please consider supporting us by signing on as a sponsor for our Roadtown Turkey Trot.</p>",
            mailing_address="PO Box 256\nShutesbury, MA 01072",
            email_address="roadtowntt@gmail.com",
            phone_number="413-259-1213",
            facebook_url="https://www.facebook.com/people/Roadtown-Turkey-Trot/100094679902568/",
            instagram_url="https://www.instagram.com/roadtowntrot/",
        )

        # Add to root page
        root_page.add_child(instance=turkey_trot_page)

        # Update site to point to our new page
        site = Site.objects.get(is_default_site=True)
        site.root_page = turkey_trot_page
        site.save()

        self.stdout.write(self.style.SUCCESS("Successfully created Turkey Trot page!"))
        self.stdout.write(self.style.SUCCESS("You can now access the Wagtail admin at /admin/"))
