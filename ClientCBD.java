package tika;

import java.io.BufferedInputStream;import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;
import org.apache.tika.detect.Detector;
import org.apache.tika.detect.NNExampleModelDetector;
import org.apache.tika.detect.TrainedModelDetector;
import org.apache.tika.metadata.Metadata;
import org.apache.tika.mime.MediaType;
import org.apache.tika.mime.MimeDetectionTest;

public class ClientCBD
{
	public static void main(String[] args) throws IOException
	{
		String classPrefix = TrainedModelDetector.class.getPackage().getName()
                .replace('.', '/')
                + "/";

        Metadata metadata = new Metadata();
        File file = new File("/home/durga/workspace/tika/tika-core/src/main/resources/org/apache/tika/detect/video-quicktime-tika.model");
        Detector detector = new NNExampleModelDetector(file);
      //  InputStream in = MimeDetectionTest.class.getResourceAsStream("test.html");
       // InputStream in = new FileInputStream("/home/durga/testfiles/help.html");
        File fileType = new File("/home/durga/testfiles");
        File[] files = fileType.listFiles();
        int count = 0;
        for(File f:files)
        {
	        InputStream in = new BufferedInputStream(new FileInputStream(f));
	        System.out.println(in.markSupported());
	        if (!in.markSupported()) {
				in = new java.io.BufferedInputStream(in);
			}
	        MediaType mimeObj = detector.detect(in, metadata);
	        String mime = mimeObj.toString();
			System.out.println(mime+"\n--------------------");
			if(mime.equals("video/quicktime"))
				count++;
        }
        System.out.println("No.of video/quicktime identified: "+count);
       // **/
        /**
        System.out.println(in.markSupported());
        if (!in.markSupported()) {
			in = new java.io.BufferedInputStream(in);
		}
        MediaType mimeObj = detector.detect(in, metadata);
        String mime = mimeObj.toString();
		System.out.println(mime+"\n--------------------");
		**/
	}
}