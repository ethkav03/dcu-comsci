import java.io.FileOutputStream;
import java.io.IOException;
import java.math.BigInteger;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.security.MessageDigest;
import java.security.SecureRandom;
import javax.crypto.Cipher;
import javax.crypto.spec.IvParameterSpec;
import javax.crypto.spec.SecretKeySpec;

public class Assignment1 {
    private static final BigInteger g = new BigInteger("44ec9d52c8f9189e49cd7c70253c2eb3154dd4f08467a64a0267c9defe4119f2e373388cfa350a4e66e432d638ccdc58eb703e31d4c84e50398f9f91677e88641a2d2f6157e2f4ec538088dcf5940b053c622e53bab0b4e84b1465f5738f549664bd7430961d3e5a2e7bceb62418db747386a58ff267a9939833beefb7a6fd68", 16);
    private static final BigInteger A = new BigInteger("5af3e806e0fa466dc75de60186760516792b70fdcd72a5b6238e6f6b76ece1f1b38ba4e210f61a2b84ef1b5dc4151e799485b2171fcf318f86d42616b8fd8111d59552e4b5f228ee838d535b4b987f1eaf3e5de3ea0c403a6c38002b49eade15171cb861b367732460e3a9842b532761c16218c4fea51be8ea0248385f6bac0d", 16);
    private static final BigInteger p = new BigInteger("b59dd79568817b4b9f6789822d22594f376e6a9abc0241846de426e5dd8f6eddef00b465f38f509b2b18351064704fe75f012fa346c5e2c442d7c99eac79b2bc8a202c98327b96816cb8042698ed3734643c4c05164e739cb72fba24f6156b6f47a7300ef778c378ea301e1141a6b25d48f1924268c62ee8dd3134745cdf7323", 16);

    public static void main(String[] args) throws Exception {
        SecureRandom random = new SecureRandom();
        BigInteger b = new BigInteger("44232056147089407306763703738586663739375881729519141764599613212356454288939976320728741314531029197922378476477680224956564296155963570480042571884987991238739240317661903599046890797310435425481730689569826421802646622350680801519236362293710210575496892332200092780292294233724409162207137127693283271404");

        // Calculate public shared value B = g^b mod p
        BigInteger B = modularExponentiation(g, b, p);
        saveToFile("DH.txt", B.toString(16));

        // Calculate the shared secret value s = A^b mod p
        BigInteger s = modularExponentiation(A, b, p);

        // Hash the shared secret value
        MessageDigest sha256 = MessageDigest.getInstance("SHA-256");
        byte[] aesKey = sha256.digest(s.toByteArray());

        byte[] iv = new byte[16];
        random.nextBytes(iv);
        saveToFile("IV.txt", bytesToHex(iv));

        // AES encryption in CBC mode
        byte[] aes = aesEncryption(aesKey, iv, "Assignment1.class");
        System.out.println(bytesToHex(aes));
    }

    // Modular Exponentiation
    private static BigInteger modularExponentiation(
        BigInteger base, 
        BigInteger exponent, 
        BigInteger modulus
    ) throws Exception {
        BigInteger result = BigInteger.ONE;
        base = base.mod(modulus);

        while (exponent.compareTo(BigInteger.ZERO) > 0) {
            // If exponent is odd, multiply the base with result
            if (exponent.testBit(0)) {
                result = result.multiply(base).mod(modulus);
            }
            // Square the base and reduce the exponent by half
            base = base.multiply(base).mod(modulus);
            exponent = exponent.shiftRight(1); // Divide exponent by 2
        }

        return result;
    }

    // AES Encryption method
    private static byte[] aesEncryption(byte[] key, byte[] iv, String inputFile) throws Exception {
        // Initialize AES in CBC mode with no padding
        Cipher cipher = Cipher.getInstance("AES/CBC/NoPadding");
        SecretKeySpec secretKeySpec = new SecretKeySpec(key, "AES");
        IvParameterSpec ivSpec = new IvParameterSpec(iv);
        cipher.init(Cipher.ENCRYPT_MODE, secretKeySpec, ivSpec);

        // Read input file and apply padding
        byte[] inputData = Files.readAllBytes(Paths.get(inputFile));
        byte[] paddedData = applyPadding(inputData, cipher.getBlockSize());

        // Encrypt the padded data
        byte[] encryptedData = cipher.doFinal(paddedData);

        return encryptedData;
    }

    // Apply custom padding
    private static byte[] applyPadding(byte[] data, int blockSize) throws Exception {
        int paddingLength = blockSize - (data.length % blockSize);
        byte[] paddedData;

        if (paddingLength == 0) {
            // Add an extra block with 1-bit and fill with 0s
            paddedData = new byte[data.length + blockSize];
            System.arraycopy(data, 0, paddedData, 0, data.length);
            paddedData[data.length] = (byte) 0x80;
        } else {
            // Apply padding with 1-bit followed by 0-bits
            paddedData = new byte[data.length + paddingLength];
            System.arraycopy(data, 0, paddedData, 0, data.length);
            paddedData[data.length] = (byte) 0x80;
        }
        return paddedData;
    }

    // Save to file
    private static void saveToFile(String filename, String data) throws IOException {
        try (FileOutputStream fos = new FileOutputStream(filename)) {
            fos.write(data.getBytes());
        }
    }

    // Convert bytes to hexadecimal string
    private static String bytesToHex(byte[] bytes) {
        StringBuilder sb = new StringBuilder();
        for (byte b : bytes) {
            sb.append(String.format("%02x", b));
        }
        return sb.toString();
    }
}
