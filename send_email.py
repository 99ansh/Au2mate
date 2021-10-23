import smtplib
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate

SERVER_NAME=""

def send_mail(send_from, send_to, cc_list, subject, text, files=None,
              server=SERVER_NAME):
    assert isinstance(send_to, list)
    assert isinstance(cc_list, list)

    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = COMMASPACE.join(send_to)
    msg['Cc'] = COMMASPACE.join(cc_list)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject

    msg.attach(MIMEText(text,'html'))

    for f in files or []:
        with open(f, "rb") as fil:
            part = MIMEApplication(
                fil.read(),
                Name=basename(f)
            )
        # After the file is closed
        part['Content-Disposition'] = 'attachment; filename="%s"' % basename(f)
        msg.attach(part)

    smtp = smtplib.SMTP(server)
    smtp.sendmail(send_from, send_to, msg.as_string())
    smtp.close()

body_text = '<div id="testcase-data-insight" style="display: block;"> Total Testcases: <span id="count-testcases"><b>41</b></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <span style="color:limegreen;">Passed: </span><span id="count-passed"><b>12</b></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <span style="color:red;">Failed: </span><span id="count-failed"><b>9</b></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <span style="color:mediumblue;">In Queue: </span> <span id="count-inqueue"><b>10</b></span> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:brown;">Running: </span><span id="count-running"><b>10</b></span></div><div id="table-content" style="display: block;"><table><tbody><tr><th>Testcases</th><th>Status</th></tr></tbody><tbody id="content"><tr><td> 59285 - GLPERSL2C01 - iLO - SNP</td><td style="color: limegreen;">Passed</td></tr><tr><td> 59293 - GLPERSL2C03 - iLO - SNP</td><td style="color: brown;">Running</td></tr><tr><td> 59295 - GLPERSL2C04 - iLO - SNP</td><td style="color: red;">Failed</td></tr><tr><td> 59297 - GLPERSL2C04 - iLO - AMS - SNP</td><td style="color: mediumblue;">In Queue</td></tr><tr><td> 59303 - GLPERSL2C05 - iLO - SNP</td><td style="color: brown;">Running</td></tr><tr><td> 59307 - GLPERSL2C06 - iLO - SNP</td><td style="color: limegreen;">Passed</td></tr><tr><td> 59309 - GLPERSL2C06 - iLO - AMS - SNP</td><td style="color: red;">Failed</td></tr><tr><td> 59315 - GLPERSL2C08 - iLO - SNP</td><td style="color: limegreen;">Passed</td></tr><tr><td> 59320 - GLPERSL2C09 - iLO - AMS - SNP</td><td style="color: brown;">Running</td></tr><tr><td> 59321 - GLPERSL2C09 - iLO - SNP</td><td style="color: brown;">Running</td></tr><tr><td> 59322 - GLPERSL2C10 - iLO - AMS - SNP</td><td style="color: brown;">Running</td></tr><tr><td> 59323 - GLPERSL2C10 - iLO - SNP</td><td style="color: brown;">Running</td></tr><tr><td> 59333 - GLPERSL2C12 - iLO - SNP</td><td style="color: brown;">Running</td></tr><tr><td> 59335 - GLPERSL2C13 - iLO - SNP</td><td style="color: red;">Failed</td></tr><tr><td> 59595 - 130GLPERS01</td><td style="color: red;">Failed</td></tr><tr><td> 59596 - 130GLPERS02</td><td style="color: red;">Failed</td></tr><tr><td> 59597 - 130GLPERS03</td><td style="color: mediumblue;">In Queue</td></tr><tr><td> 59598 - 130GLPERS04</td><td style="color: limegreen;">Passed</td></tr><tr><td> 59599 - 130GLPERS05</td><td style="color: mediumblue;">In Queue</td></tr><tr><td> 59600 - 130GLPERS06</td><td style="color: mediumblue;">In Queue</td></tr><tr><td> 59601 - 130GLPERS07</td><td style="color: limegreen;">Passed</td></tr><tr><td> 59602 - 130GLPERS08</td><td style="color: red;">Failed</td></tr><tr><td> 59603 - 130GLPERS09Field LabelField ValueField LabelField Value</td><td style="color: red;">Failed</td></tr><tr><td> 59604 - 130GLPERS10</td><td style="color: limegreen;">Passed</td></tr><tr><td> 59605 - 130GLPERS11Field LabelField ValueField LabelField Value</td><td style="color: red;">Failed</td></tr><tr><td> 59606 - 130GLPERS12</td><td style="color: limegreen;">Passed</td></tr><tr><td> 59607 - 130GLPERS13</td><td style="color: mediumblue;">In Queue</td></tr><tr><td> 59608 - 130GLPERS14</td><td style="color: mediumblue;">In Queue</td></tr><tr><td> 59609 - 130GLPERS15</td><td style="color: limegreen;">Passed</td></tr><tr><td> 59610 - 130GLPERS16</td><td style="color: mediumblue;">In Queue</td></tr><tr><td> 59611 - 130GLPERS17</td><td style="color: limegreen;">Passed</td></tr><tr><td> 59612 - 130GLPERS18</td><td style="color: red;">Failed</td></tr><tr><td> 59613 - 130GLPERS19</td><td style="color: mediumblue;">In Queue</td></tr><tr><td> 59614 - 130GLPERS20</td><td style="color: brown;">Running</td></tr><tr><td> 59615 - 130GLPERS21</td><td style="color: mediumblue;">In Queue</td></tr><tr><td> 59616 - 130GLPERS22</td><td style="color: limegreen;">Passed</td></tr><tr><td> 59617 - 130GLPERS23</td><td style="color: mediumblue;">In Queue</td></tr><tr><td> 59618 - 130GLPERS24</td><td style="color: brown;">Running</td></tr><tr><td> 59619 - 130GLPERS25</td><td style="color: brown;">Running</td></tr><tr><td> 59620 - 130GLPERS26</td><td style="color: limegreen;">Passed</td></tr><tr><td> 59621 - 130GLPERS27</td><td style="color: limegreen;">Passed</td></tr></tbody></table></div>'
output_str = f'<!DOCTYPE html><html><head><style></style></head><body>{body_text}</body></html>'

send_mail(send_from="aryancountry@gmail.com",
          send_to=["99ansh@gmail.com"],
          cc_list=["aryan.mehta@hpe.com"],
          subject="Test",
          text=output_str)
